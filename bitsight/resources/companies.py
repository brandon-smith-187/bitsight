def get_findings(self, guid):
    """
    Get all findings for a company
    :param guid: the BitSight guid for the company
    :return: json representation of all applicable findings
    """
    request_url = self.COMPANIES_ENDPOINT + guid + "/findings"
    first = self._get_request_handler(
        request_url
    )
    response = first.json()
    findings = response[RESULTS]
    while response[LINKS][NEXT]:
        response = self._get_request_handler(
            response[LINKS][NEXT], cookies=first.cookies
        ).json()
        findings.extend(response[RESULTS])
    return findings
