from django.conf import settings
from django.apps import apps


def get_code_form_submission(submission_pk):
    """Just returns code from submission instance"""
    Submission = apps.get_model("submission_app", "Submission")
    return Submission.objects.get(pk=submission_pk).code


class PromptBuilder:
    """Simple base prompt builder based on settings"""

    prompt_template = "{base_prompt} \n {user_prompt}"
    base_prompt = settings.OPENAI_USER_PROMPT

    def __init__(self, user_prompt, base_prompt=None):
        if not base_prompt:
            self.base_prompt = base_prompt

        self.user_prompt = user_prompt

    def get_context(self):
        return {"base_prompt": self.base_prompt, "user_prompt": self.user_prompt}

    def __call__(self, *args, **kwargs):
        return self.prompt_template.format(**self.get_context())
