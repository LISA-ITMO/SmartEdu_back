from subprocess import Popen
from tempfile import TemporaryDirectory
from io import BytesIO


class BaseCodeExecutor:
    """Base class to execute and control code in docker container by tag"""

    default_filename = "source_code"
    file_prefix = ""

    image_tag: None | str = None
    temp_folder: None | TemporaryDirectory = None

    run_command: None | str = None
    compile_command: None | str = None
    docker_command = (
        'docker run --mount type=bind,source={temp_folder},target="/media" {tag}'
    )

    def __init__(self, code: str):
        self.code = code
        if not self.temp_folder:
            self.temp_folder = TemporaryDirectory()

    def get_tag(self):
        """Can use for getting image by id or etc. (You can create images)"""
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
        return self.temp_folder.name

    def execute(self, stdin=None):
        """
        Execute initial code with given stdin
        :param stdin: input data for code, usually it's should be str
        :return: status code of process.
        """
        self.write_file_to_temp("stdin", stdin)
        self.create_code_file()

        docker_runner = Popen(
            self.format_string(self.docker_command) + " " + self.get_exec_command(),
            shell=True,
        )
        docker_runner.wait()

        return docker_runner.returncode

    def get_run_command(self):
        """get function for formatting and adding stream redirection"""
        return (
            f'"{self.run_command.format(**self.get_context()) + " < stdin > stdout"}"'
        )

    def get_compile_command(self):
        if self.compile_command:
            return self.compile_command.format(**self.get_context())
        return None

    def get_exec_command(self):
        return " && ".join(
            filter(
                lambda d: d is not None,
                [self.get_compile_command(), self.get_run_command()],
            )
        )

    def get_filename(self, filename: str):
        return self.temp_folder_name + "/" + filename

    def get_context(self) -> dict:
        """Returns dict with a context to format string"""
        return {
            "max_mem": self.max_mem,
            "max_realtime": self.max_realtime,
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
# TODO: make mixin for mesuring
# TODO: make tests :(
# TODO: write docs for this class
