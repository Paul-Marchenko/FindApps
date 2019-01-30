*UI python tests*
`How to run tests:`

pytest <test(s) location> --browser <browser name>
E.g.: pytest tests/test_job_page.py --browser chrome 

`Run tests with different marks:`
pytest <test(s) location> --browser <browser name> -m <mark>
E.g.: pytest tests/test_job_page.py --browser chrome -m sanity