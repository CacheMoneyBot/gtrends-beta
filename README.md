
## Gtrends-beta

The script pulls 'interest-over-time' queries from Google Trends and utilizes the new word disambiguation features of Gtrends Beta (2013 Q4). Matches on financial firms, investment firms etc then by fuzzy string matching.


The program inputs the original search term and disambiguates between various
entity types, then returns the correct company/corporate type matched by phrase similarity. In case there are multiple company types (e.g. Wachovia Securities, Wachovia Group).

Occasionally when the entity name does not match original search term, it is because the company has changed name and Google Trends actually returns the new company name/parent company.



### INSTRUCTIONS:
pip install -r requirements.txt


Requires:
- Google account
- PhantomJS + Selenium webdriver if running this program over remote servers. Google sometimes requires mobile authentication when loggin in from new locations/IPs.


Arch Linux:
    sudo pacman -S phantomjs

Ubuntu:
    sudo apt-get install phantomjs

OS X:
    sudo brew install phantomjs

**Python 2 not supported.


#### EXAMPLE COMMANDS TO EXECUTE
export GMAIL_USER="username@gmail.com"
export base_dir="$HOME/gtrends-beta"


#####Single Keyword to stdout
Disambiguation features:
Define valid entity types in __entity_types.py__. Currently filters for companies and investment banking firms. Tesla returns Teslam Motors queries rather than Nikola Tesla or tesla coils for example.

    python3 $base_dir/google_trends/trends.py \
        --username $GMAIL_USER \
        --password justfortesting! \
        --keyword "Tesla"  \
        --start-date 2012-03 --end-date 2012-06


#####Category filters: BofA Merrill Lynch -> Category 0-7 (Finance)
    python3 $base_dir/google_trends/trends.py \
        --username $GMAIL_USER \
        --password justfortesting! \
        --keyword "BofA Merrill Lynch" \
        --throttle "random" \
        --category 0-7




##### Quarterly queries -6 +24 months around a date.

    python3 $base_dir/google_trends/trends.py \
        --username $GMAIL_USER \
        --password justfortesting! \
        --quarterly "2012-05" \
        --keyword "Facebook"


Iterates quarterly queries (for daily data) then merges with long term trends data through interpolation (log10 changes in daily interest).


![alt tag](http://url/to/img.png)


#####Batch input from a text file
!Deprecated, use

    python3 $base_dir/google_trends/trends.py \
        --username $GMAIL_USER \
        --password justfortesting! --throttle "random" \
        --file $base_dir/input-files/test.txt  \
        --start-date 2013-01 --end-date 2013-6 \
        --category 0-7-107


#####Batch input/output to a set directory, names files according to date ranges and categories
    python3 $base_dir/google_trends/trends.py \
        --username $GMAIL_USER \
        --password justfortesting! \
        --throttle "random" \
        --file $base_dir/input-files/test.txt  \
        --output $base_dir/underwriters/0-12-784-business-news \
        --category 0-7-784 \
        --start-date "2004-01" --end-date "2013-12" \


### Data Format:
CSV header:
Date, Entity Name, Entity Type, Original Search Term



##### Finance Categories

    0-12: Business & Industrial
        0-12-1138: Business Finance
            0-12-1138-1160: Commercial Lending
            0-12-1138-1139: Investment Banking
            0-12-1138-620: Risk Management
            0-12-1138-905: Venture Capital
        0-12-784: Business News
            0-12-784-1179: Company News
                0-12-784-1179-1240: Company Earnings
                0-12-784-1179-1241: Mergers & Acquisitions
            0-12-784-1164: Economy News
            0-12-784-1163: Financial Markets
            0-12-784-1165: Fiscal Policy News
    0-7: Finance
        0-7-278: Accounting & Auditing
            0-7-278-1341: Accounting & Financial Software
            0-7-278-1283: Tax Preparation & Planning
        0-7-37: Banking
        0-7-279: Credit & Lending
            0-7-279-468: Auto Financing
            0-7-279-813: College Financing
            0-7-279-811: Credit Cards
            0-7-279-812: Debt Management
            0-7-279-466: Home Financing
        0-7-814: Currencies & Foreign Exchange
        0-7-903: Financial Planning
        0-7-1282: Grants & Financial Assistance
            0-7-1282-813: College Financing
        0-7-38: Insurance
            0-7-38-467: Auto Insurance
            0-7-38-249: Health Insurance
            0-7-38-465: Home Insurance
        0-7-107: Investing
            0-7-107-904: Commodities & Futures Trading
        0-7-619: Retirement & Pension






