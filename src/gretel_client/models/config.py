from abc import ABC, abstractmethod
from typing import Dict, Optional

StatusDescriptions = Dict[str, Dict[str, str]]


CPU = "cpu"
GPU = "gpu"


def get_status_description(
    descriptions: StatusDescriptions, status: str, runner: str
) -> str:
    status_desc = descriptions.get(status)
    if not status_desc:
        return ""
    return status_desc.get(runner, status_desc.get("default", ""))


class ModelTypeConfig(ABC):
    @property
    @abstractmethod
    def action_name(self) -> Optional[str]:
        ...

    @property
    def train_instance_type(self) -> str:
        return CPU

    @property
    def run_instance_type(self) -> str:
        return CPU

    @property
    @abstractmethod
    def run_status_descriptions(self) -> StatusDescriptions:
        ...

    @property
    def train_status_descriptions(self) -> StatusDescriptions:
        return {
            "created": {
                "default": "Model creation has been queued.",
            },
            "pending": {
                "default": "A worker is being allocated to begin model creation.",
                "cloud": "A Gretel Cloud worker is being allocated to begin model creation.",
                "local": "A local container is being started to begin model creation.",
            },
            "active": {
                "default": "A worker has started creating your model!",
            },
        }

    @abstractmethod
    def peek_report(self, report_contents: dict) -> Optional[dict]:
        ...


class GenericModelTypeConfig(ModelTypeConfig):
    @property
    def action_name(self) -> Optional[str]:
        return None

    @property
    def run_status_descriptions(self) -> StatusDescriptions:
        return {
            "created": {
                "default": "A job has been queued.",
            },
            "pending": {
                "default": "A worker is being allocated to begin running.",
                "cloud": "A Gretel Cloud worker is being allocated",
                "local": "A local container is being started.",
            },
            "active": {
                "default": "A worker has started!",
            },
        }

    def peek_report(self, report_contents: dict) -> Optional[dict]:
        return None


class TransformsModelTypeConfig(ModelTypeConfig):
    @property
    def action_name(self) -> Optional[str]:
        return "transform"

    @property
    def run_status_descriptions(self) -> StatusDescriptions:
        return {
            "created": {
                "default": "A Record transform job has been queued.",
            },
            "pending": {
                "default": "A worker is being allocated to begin running a transform pipeline.",
                "cloud": "A Gretel Cloud worker is being allocated to begin transforming records.",
                "local": "A local container is being started to and will begin transforming records.",
            },
            "active": {
                "default": "A worker has started!",
            },
        }

    def peek_report(self, report_contents: dict) -> Optional[dict]:
        fields = [
            "training_time_seconds",
            "record_count",
            "field_count",
            "field_transforms",
            "value_transforms",
        ]
        return {f: report_contents[f] for f in fields}


class ClassifyModelTypeConfig(ModelTypeConfig):
    @property
    def action_name(self) -> Optional[str]:
        return "classify"

    @property
    def run_status_descriptions(self) -> StatusDescriptions:
        return {
            "created": {
                "default": "A Record classify job has been queued.",
            },
            "pending": {
                "default": "A worker is being allocated to begin running a classification pipeline.",
                "cloud": "A Gretel Cloud worker is being allocated to begin classifying records.",
                "local": "A local container is being started and will begin classifying records.",
            },
            "active": {
                "default": "A worker has started!",
            },
        }

    def peek_report(self, report_contents: dict) -> Optional[dict]:
        fields = ["elapsed_time_seconds", "record_count", "field_count", "warnings"]
        return {f: report_contents[f] for f in fields}


class SyntheticsModelTypeConfig(ModelTypeConfig):
    @property
    def action_name(self) -> Optional[str]:
        return "generate"

    @property
    def train_instance_type(self) -> str:
        return GPU

    @property
    def run_status_descriptions(self) -> StatusDescriptions:
        return {
            "created": {
                "default": "A Record generation job has been queued.",
            },
            "pending": {
                "default": "A worker is being allocated to begin generating synthetic records.",
                "cloud": "A Gretel Cloud worker is being allocated to begin generating synthetic records.",
                "local": "A local container is being started to begin record generation.",
            },
            "active": {
                "default": "A worker has started!",
            },
        }

    def peek_report(self, report_contents: dict) -> Optional[dict]:
        fields = [
            "synthetic_data_quality_score",
            "field_correlation_stability",
            "principal_component_stability",
            "field_distribution_stability",
            "privacy_protection_level",
        ]
        return {f: report_contents[f] for f in fields if f in report_contents}


_CONFIGS = {
    "synthetics": SyntheticsModelTypeConfig(),
    "transforms": TransformsModelTypeConfig(),
    "classify": ClassifyModelTypeConfig(),
    "__default__": GenericModelTypeConfig(),
}


def get_model_type_config(model_type: Optional[str] = None) -> ModelTypeConfig:
    if model_type is None:
        return _CONFIGS["__default__"]

    return _CONFIGS.get(model_type, _CONFIGS["__default__"])