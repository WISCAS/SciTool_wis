import re
url1 ='''<a href="https://doi.org/10.22184/1992-4178.2018.174.3.134.136">
<i class="icon-external-link"></i>
                      https://doi.org/10.22184/1992-4178.2018.174.3.134.136
                    </a>'''
def download_url(doi_org):
    libgen_header = "http://libgen.io/scimag/ads.php?doi="
    libgen_tailor = "&downloadname="
    doi = re.findall(r'\S(https://doi.org/[a-zA-Z0-9/\.\-?]+)', doi_org, re.S)
    dl_url = libgen_header+doi[0]+libgen_tailor
    print(dl_url)
    return dl_url
download_url(url1)