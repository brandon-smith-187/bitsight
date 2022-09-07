import datetime
# import pandas
import os
from concurrent.futures import ThreadPoolExecutor, as_completed

import bitsight

if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    # companies_endpoint = bitsight.Companies()
    # findings = companies_endpoint.get_findings('97a6a734-b16f-47c2-a3c1-4f08358821a3')
    # pp(findings)
    # print(len(findings))

    # reports = bitsight.Reports()
    # pdf = reports.post_download_company_report('97a6a734-b16f-47c2-a3c1-4f08358821a3')
    # pp(pdf)

    # risk_vectors = companies_endpoint.get_company_details('97a6a734-b16f-47c2-a3c1-4f08358821a3')
    # pp(risk_vectors)

    # portfolio = bitsight.Portfolio()
    # companies = portfolio.get_portfolio(folder='54dbf2a8-f82c-4fdf-9bf0-ae0080a6774d')
    # pp(folder_details)

    # df = pandas.json_normalize(companies)
    # df.to_excel('folder_export2.xlsx')
    #
    # times = []
    # for company in companies:
    #     start_time = datetime.datetime.now()
    #     companies_endpoint.get_findings(guid=company['guid'])
    #     times.append(datetime.datetime.now() - start_time)
    #     print(f"Completed: {company['name']}")
    #
    # print(f'Min: {min(times)}')
    # print(f'Max: {max(times)}')
    # print(f'Average: {sum(times, datetime.timedelta())/len(times)}')

    start_time = datetime.datetime.now()

    portfolio = bitsight.Portfolio()
    companies = bitsight.Companies()
    portfolio_companies = portfolio.get_portfolio(folder='54dbf2a8-f82c-4fdf-9bf0-ae0080a6774d')

    lst = []
    max_threads = (
        3
    )
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        results = {executor.submit(companies.get_findings, company['guid']): company for company in portfolio_companies}

        for company in as_completed(results.keys()):
            result = company.result()
            if result:
                print(results[company]['name'])
                # lst.append([result, results[company]])

    # pp(lst)

    end_time = datetime.datetime.now() - start_time
    print("Execution time: ", end_time, " (hour:minute:second:microsecond)")
