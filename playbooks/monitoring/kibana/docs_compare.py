'''
Usage:
  python docs_compare.py /path/to/internal/docs /path/to/metricbeat/docs
'''

from docs_compare_util import check_parity

allowed_deletions_from_metricbeat_docs_extra = [
  # 'path.to.field'
  'kibana_stats.response_times.max',
  'kibana_stats.response_times.average'
]

def handle_special_case_kibana_settings(internal_doc, metricbeat_doc):
  # Internal collection will index kibana_settings.xpack.default_admin_email as null
  # whereas Metricbeat collection simply won't index it. So if we find kibana_settings.xpack.default_admin_email 
  # is null, we simply remove it
  if "xpack" in internal_doc["kibana_settings"] \
    and "default_admin_email" in internal_doc["kibana_settings"]["xpack"] \
    and internal_doc["kibana_settings"]["xpack"]["default_admin_email"] == None:
    internal_doc["kibana_settings"]["xpack"].pop("default_admin_email")

def handle_special_cases(doc_type, internal_doc, metricbeat_doc):
    if doc_type == "kibana_settings":
        handle_special_case_kibana_settings(internal_doc, metricbeat_doc)


check_parity(handle_special_cases, allowed_deletions_from_metricbeat_docs_extra=allowed_deletions_from_metricbeat_docs_extra)
