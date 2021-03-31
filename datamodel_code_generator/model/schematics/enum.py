from typing import ClassVar

from datamodel_code_generator.model.schematics import BaseModel


class SchematicsEnum(BaseModel):
    TEMPLATE_FILE_PATH: ClassVar[str] = 'schematics/Enum.jinja2'
    BASE_CLASS: ClassVar[str] = ''
