from __future__ import annotations

from pathlib import Path
from typing import Optional, Union

from gretel_client.config import get_session_config, RunnerMode
from gretel_client.evaluation.reports import BaseReport, ReportDictType
from gretel_client.projects.common import DataSourceTypes, RefDataTypes
from gretel_client.projects.projects import Project


class TextQualityReport(BaseReport):
    """Represents a Text Quality Report (Text SQS). This class can be used to create a report.

    Args:
        project: Optional project associated with the report. If no project is passed, a temp project (:obj:`gretel_client.projects.projects.tmp_project`) will be used.
        data_source: Data source used for the report.
        ref_data: Reference data used for the report.
        output_dir: Optional directory path to write the report to. If the directory does not exist, the path will be created for you.
        runner_mode: Determines where to run the model. See :obj:`gretel_client.config.RunnerMode` for a list of valid modes. Manual mode is not explicitly supported.
        target: The field used for assessing quality.  Must be present in both data_source and ref_data.  If None, we attempt to choose the "best" field.
    """

    _model_dict: dict = {
        "schema_version": "1.0",
        "name": "evaluate-text-quality",
        "models": [
            {
                "evaluate": {
                    "task": {"type": "text"},
                    "data_source": "__tmp__",
                    "params": {
                        "target": None,
                    },
                },
            }
        ],
    }

    @property
    def model_config(self) -> dict:
        return self._model_dict

    @property
    def base_artifact_name(self) -> str:
        return "text_metrics_report"

    def __init__(
        self,
        *,
        target: Optional[str] = None,
        project: Optional[Project] = None,
        name: Optional[str] = None,
        data_source: DataSourceTypes,
        ref_data: RefDataTypes,
        output_dir: Optional[Union[str, Path]] = None,
        runner_mode: Optional[RunnerMode] = None,
    ):
        runner_mode = runner_mode or get_session_config().default_runner

        if runner_mode == RunnerMode.MANUAL:
            raise ValueError(
                "Cannot use manual mode. Please use CLOUD, LOCAL, or HYBRID."
            )

        # Update the model name if one was provided
        if name is not None:
            self._model_dict["name"] = name

        # Update the target if one was provided
        if target is not None:
            self._model_dict["models"][0]["evaluate"]["params"]["target"] = target

        super().__init__(project, data_source, ref_data, output_dir, runner_mode)

    def peek(self) -> Optional[ReportDictType]:
        super()._check_model_run()
        if self._report_dict:
            return self._report_dict.get("synthetic_data_quality_score")
