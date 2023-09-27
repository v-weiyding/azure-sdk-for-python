# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

from datetime import datetime, timedelta
from typing import Dict, Optional

from azure.ai.ml._restclient.v2023_04_01_preview.models import FeaturesetJob as RestFeaturesetJob
from azure.ai.ml._utils._experimental import experimental
from azure.ai.ml.entities._mixins import RestTranslatableMixin
from azure.ai.ml.entities._system_data import SystemData

from .materialization_type import MaterializationType

FeaturestoreJobTypeMap: Dict[str, MaterializationType] = {
    "BackfillMaterialization": MaterializationType.BACKFILL_MATERIALIZATION,
    "RecurrentMaterialization": MaterializationType.RECURRENT_MATERIALIZATION,
}


@experimental
class FeatureSetMaterializationMetadata(RestTranslatableMixin):
    """Feature Set Materialization Metadata

    :param type: The type of the materialization job.
    :type type: MaterializationType
    :param feature_window_start_time: The feature window start time for the feature set materialization job.
    :type feature_window_start_time: Optional[datetime]
    :param feature_window_end_time: The feature window end time for the feature set materialization job.
    :type feature_window_end_time: Optional[datetime]
    :param name: The name of the feature set materialization job.
    :type name: Optional[str]
    :param display_name: The display name for the feature set materialization job.
    :type display_name: Optional[str]
    :param creation_context: The creation context of the feature set materialization job.
    :type creation_context: Optional[~azure.ai.ml.entities.SystemData]
    :param duration: current time elapsed for feature set materialization job.
    :type duration: Optional[~datetime.timedelta]
    :param status: The status of the feature set materialization job.
    :type status: Optional[str]
    :param tags: Tag dictionary. Tags can be added, removed, and updated.
    :type tags: Optional[dict[str, str]]
    :param kwargs: A dictionary of additional configuration parameters.
    :type kwargs: dict
    """

    def __init__(
        self,
        *,
        type: MaterializationType,  # pylint: disable=redefined-builtin
        feature_window_start_time: Optional[datetime],
        feature_window_end_time: Optional[datetime],
        name: Optional[str],
        display_name: Optional[str],
        creation_context: Optional[SystemData],
        duration: Optional[timedelta],
        status: Optional[str],
        tags: Optional[Dict[str, str]],
        **kwargs  # pylint: disable=unused-argument
    ) -> None:
        self.type = type
        self.feature_window_start_time = feature_window_start_time
        self.feature_window_end_time = feature_window_end_time
        self.name = name
        self.display_name = display_name
        self.creation_context = creation_context
        self.duration = duration
        self.status = status
        self.tags = tags

    @classmethod
    def _from_rest_object(cls, obj: RestFeaturesetJob) -> "FeatureSetMaterializationMetadata":
        if not obj:
            return None
        return FeatureSetMaterializationMetadata(
            type=FeaturestoreJobTypeMap.get(obj.type),
            feature_window_start_time=obj.feature_window.feature_window_start,
            feature_window_end_time=obj.feature_window.feature_window_end,
            name=obj.job_id,
            display_name=obj.display_name,
            creation_context=SystemData(created_at=obj.created_date),
            duration=obj.duration,
            status=obj.status,
            tags=obj.tags,
        )
