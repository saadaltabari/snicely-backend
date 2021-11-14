from googleapiclient import discovery

from settings import SETTINGS


__PERSPECTIVE_SERVICE = discovery.build(
    'commentanalyzer',
    'v1alpha1',
    developerKey=SETTINGS['PERSPECTIVE_API_KEY'],
    discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
    static_discovery=False
)


class ToxicityHandler:
    """
    Evaluate whether text written by user
    is toxic or not.
    """

    def __init__(self, user_text):
        self.user_text = user_text

    def _get_service(self):
        """
        Retrieve the service for assessing text toxicity
        """
        raise NotImplementedError

    def _call_service(self):
        """
        Call the service for assessing text toxicity
        Returns
        -------
        Service specific result
        """
        raise NotImplementedError

    def _get_service_request_body(self):
        """
        Define the HTTP JSON body for calling
        the toxicity assessment service
        Returns
        -------
        json object
        """
        raise NotImplementedError

    def _process_toxic_text(self, service_response):
        """
        process the result returned form toxic text
        assessment service
        Parameters
        ----------
        service_response: json object

        Returns
        -------
        """
        raise NotImplementedError

    def evaluate(self):
        """
        Retrieve the toxicity socre of user_text from
        the perspective API

        Returns
        -------
        bool indicating if the user text is contains toxic language
        obj the result of processing the result returned from the service
        """

        response = self._call_service()

        toxic_text = self._process_toxic_text(service_response=response)

        if toxic_text:
            return True, toxic_text
        return False, None


class PerspectiveAPIToxicityHandler(ToxicityHandler):

    def _process_toxic_text(self, service_response):
        toxic_text = []
        for highlighted_text in response.get('attributeScores', {}).get('TOXICITY', {}).get('spanScores', []):
            begin = highlighted_text['begin']
            end = highlighted_text['end']
            toxic_text.append({
                'text': text[begin:end],
                'begin': begin,
                'end': end
            })
        return toxic_text

    def _get_service_request_body(self):
        return {
            'comment': {
                'text': self.user_text
            },
            'requestedAttributes': {
                'TOXICITY': {
                    'scoreThreshold': SETTINGS['TOXICITY_THRESHOLD']
                },
            },
            'spanAnnotations': True
        }

    def _call_service(self):
        return self._get_service()\
            .comments().analyze(
                body=self._get_service_request_body()
            ).execute()

    def _get_service(self):
        return __PERSPECTIVE_SERVICE
