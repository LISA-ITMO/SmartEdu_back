from subprocess import Popen
from tempfile import TemporaryDirectory
from io import BytesIO


class BaseCodeExecutor:
    """
    Base class to execute and control code in docker container by tag

    This class has his own context which represents by dictionary.

    Context:
        context = {
            "filename": default file name of source code,
                "temp_folder": path to tempfolder,
                "tag": docker container tag,
            }


    Attributes:
        default_filename: default file name to run code
        file_prefix: file prefix which adds for source_code
        image_tag: docker's container tag to execute code
        temp_folder: temp directory for binding to docker container, if not set it's create new every time
        run_command: string to format for running code
        compile_command: string to format for compiling code
        docker_command: string to format for start docker container

    """

    default_filename = "source_code"
    file_prefix = ""

    image_tag: None | str = None
    temp_folder: None | TemporaryDirectory = None

    run_command: None | str = None
    compile_command: None | str = None
    docker_command = 'docker run --stop-timeout 100 --mount type=bind,source={temp_folder},target="/media" {tag}'

    def __init__(self, code: str):
        """
        :param code: Initial code to execute with given command
        """
        self.code = bytes(code, "UTF-8")
        if not self.temp_folder:
            self.temp_folder = TemporaryDirectory()

    def get_tag(self) -> str:
        """
        Can use for getting image by id or etc. (You can create images)
        :return: image tag for docker container
        """
        return self.image_tag

    def create_code_file(self):
        """Creates file with user's source code"""
        self.write_file_to_temp(self.default_filename + self.file_prefix, self.code)

    def write_file_to_temp(self, filename, data):
        """Writes file with data to temp directory"""
        with open(self.get_filename(filename), "wb") as file:
            file.write(data)

    @property
    def temp_folder_name(self):
        """full path to folder"""
        return self.temp_folder.name

    def execute(self, stdin=None):
        """
        Execute initial code with given stdin
        :param stdin: input data for code, usually it's should be str
        :return: status code of process.
        """
        self.write_stdin(stdin)

        self.create_code_file()

        docker_runner = Popen(
            self.format_string(self.docker_command) + " " + self.get_exec_command(),
            shell=True,
        )
        docker_runner.wait()

        return docker_runner.returncode

    def write_stdin(self, stdin: bytes):
        """
        Writes stdin to file if represented. Else writes blank file
        :param stdin: bytes string
        :return: None
        """
        if stdin:
            self.write_file_to_temp("stdin", stdin)
        else:
            self.write_file_to_temp("stdin", b"")

    def get_run_command(self):
        """get function for formatting and adding stream redirection"""
        return (
            f'"{self.run_command.format(**self.get_context()) + " < stdin > stdout"}"'
        )

    def get_compile_command(self) -> str | None:
        """
        Returns command for compiling source code
        :return: None if compile command is not set
        """
        if self.compile_command:
            return self.compile_command.format(**self.get_context())
        return None

    def get_exec_command(self) -> str:
        """
        Returns full command to run programm
        :return: str
        """
        return " && ".join(
            filter(
                lambda d: d is not None,
                [self.get_compile_command(), self.get_run_command()],
            )
        )

    def get_filename(self, filename: str) -> str:
        """
        Function returns full path for file based on temp dirrectory
        :param filename: name of file
        :return: str: full path to file
        """
        return self.temp_folder_name + "/" + filename

    def get_context(self) -> dict:
        """Returns dict with a context to format string"""
        return {
            "filename": self.default_filename + self.file_prefix,
            "temp_folder": self.temp_folder_name,
            "tag": self.get_tag(),
        }

    def get_stdout(self) -> BytesIO:
        """Returns `stdout` file as BytesIO"""
        with open(self.get_filename("stdout"), "rb") as file:
            return BytesIO(file.read())

    def format_string(self, string: str):
        """Format given string with class context"""
        return string.format(**self.get_context())


class ConcretePythonCodeExecutor(BaseCodeExecutor):
    run_command = "python3.11 {filename}"
    image_tag = "sandbox"


# TODO: make refactor with some dirty funcs
# TODO: make mixin to compile and run in different containers (if it's works idk)
# TODO: make tests :(
# TODO: write docs for this class
