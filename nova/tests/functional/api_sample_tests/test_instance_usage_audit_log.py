# Copyright 2012 Nebula, Inc.
# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from six.moves import urllib

from nova.tests.functional.api_sample_tests import api_sample_base


class InstanceUsageAuditLogJsonTest(api_sample_base.ApiSampleTestBaseV21):
    ADMIN_API = True
    extension_name = "os-instance-usage-audit-log"

    def test_show_instance_usage_audit_log(self):
        response = self._do_get('os-instance_usage_audit_log/%s' %
                                urllib.parse.quote('2012-07-05 10:00:00'))
        self._verify_response('inst-usage-audit-log-show-get-resp',
                              {}, response, 200)

    def test_index_instance_usage_audit_log(self):
        response = self._do_get('os-instance_usage_audit_log')
        self._verify_response('inst-usage-audit-log-index-get-resp',
                              {}, response, 200)
