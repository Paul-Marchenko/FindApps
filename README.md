**UI python tests**

*How to run tests:*

- Run tests with: 

`pytest <test(s) location> --browser <browser name>`

E.g.: `pytest tests/test_job_page.py --browser chrome`

- Run tests with different marks:

`pytest <test(s) location> --browser <browser name> -m <mark>`

E.g.: `pytest tests/test_job_page.py --browser chrome -m sanity`

- Run tests with different marks:

`pytest <test(s) location> --run_type <type of running> (can be local or remote)`

E.g.: `pytest tests/test_job_page.py --run_type remote`

- Run with docker-compose
`docker-compose -f /path/to/docker-compose.yml up -d`
`docker-compose -f /path/to/docker-compose.yml down`


