from __future__ import absolute_import


class Segments(object):
    base_api_url = "api/segments"

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self, **kwargs):
        """
        List all segments

        Get all segments in an account.

        :param int limit: An account can have at most a 250 segments
        :param int page: Page number, defaults to 1
        """

        available_params = ["limit", "page"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request("GET", self.base_api_url, query_params).json()

    def get_subscribers(self, segment_id, **kwargs):
        if not isinstance(segment_id, int):
            raise ValueError("Segment ID are not valid.")

        available_params = ["filter", "limit", "after"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request(
            "GET", "{}/{}".format(self.base_api_url, segment_id), query_params
        ).json()

    def update(self, segment_id, name):
        if len(name) > 255:
            raise ValueError("Segment name cannot exceed 255 characters.")

        params = locals()
        body_params = {"name": name}

        response = self.api_client.request(
            "PUT", "{}/{}".format(self.base_api_url, segment_id), body=body_params
        )

        return True if response.status_code == 200 else False

    def delete(self, segment_id):
        if not isinstance(segment_id, int):
            raise ValueError("Segment ID are not valid.")

        response = self.api_client.request(
            "DELETE", "{}/{}".format(self.base_api_url, segment_id)
        )

        return True if response.status_code == 204 else False
