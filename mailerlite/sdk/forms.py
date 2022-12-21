from __future__ import absolute_import

class Forms(object):

    # Automations base API uri
    base_api_url = "api/forms"

    def __init__(self, api_client):
        self.api_client = api_client

    def list(self, type, **kwargs):
        """
        Lists all automations on account
        Ref: https://developers.mailerlite.com/docs/forms.html#list-all-forms

        :param **kwargs: You can pass additional arguments - page, limit, sort or to filter by name
        :raises: :class: `TypeError` : Got an unknown argument
        :return: JSON array
        :rtype: dict
        """

        available_params = ["limit", "page", "filter", "sort"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request(
            "GET", "{}/{}".format(self.base_api_url, type), query_params
        ).json()

    def get(self, form_id):
        """
        Get a form

        Returns information about single form.
        Ref: https://developers.mailerlite.com/docs/forms.html#get-a-form

        :param form_id: int Form ID
        :return: JSON array
        :rtype: dict
        """

        return self.api_client.request(
            "GET", "{}/{}".format(self.base_api_url, form_id)
        ).json()

    def update(self, form_id, name):
        """
        Update a form

        Provides ability to update existing form.
        Ref: https://developers.mailerlite.com/docs/forms.html#update-a-form

        :param form_id: int Form ID
        :param name: string Maximum length of 255 characters
        :return: JSON array
        :rtype: dict
        """

        body_params = {"name": name}

        return self.api_client.request(
            "PUT", "{}/{}".format(self.base_api_url, form_id), body=body_params
        ).json()

    def get_subscribers(self, form_id, **kwargs):
        """
        Get subscribers who signed up to a specific form

        Provides a list of subscribers who signed up to a specific form.
        Ref: https://developers.mailerlite.com/docs/forms.html#get-subscribers-who-signed-up-to-a-specific-form

        :param form_id: int Form ID
        :param **kwargs: dict You can pass additional arguments - page, limit or to filter by status
        :raises: :class: `TypeError` : Got an unknown argument
        :return: `true` if action was successful, `false` if field was not found
        :rtype: bool
        """

        available_params = ["limit", "page", "filter"]

        params = locals()
        query_params = {}
        for key, val in params["kwargs"].items():
            if key not in available_params:
                raise TypeError("Got an unknown argument '%s'" % key)
            query_params[key] = val

        return self.api_client.request(
            "GET", "{}/{}/subscribers".format(self.base_api_url, form_id), query_params
        ).json()

    def delete(self, form_id):
        """
        Delete a form

        Provides ability to delete a form.
        Ref: https://developers.mailerlite.com/docs/forms.html#delete-a-form

        :param form_id: int Form ID
        :return: `true` if action was successful, `false` if field was not found
        :rtype: bool
        """

        response = self.api_client.request(
            "DELETE", "{}/{}".format(self.base_api_url, form_id)
        )

        return True if response.status_code == 204 else False
