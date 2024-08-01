from setuptools import find_packages, setup

setup(
    name='Flare Beacon',
    version='0.4',
    platforms=["any"],  # or more specific, e.g. "win32", "cygwin", "osx"
    license="""MIT License

    Copyright (c) 2016 Austin Taylor

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.""",
    long_description='Flare Beacon is a network analytic framework designed for data scientists, security researchers, and network professionals. Written in Python, it is designed for rapid prototyping and development of behavioral analytics, and intended to make identifying malicious behavior in networks as simple as possible.',
    packages=find_packages(),
    scripts=['bin/hextoip', 'bin/iptohex', 'bin/ipwhois', 'bin/flare_beacon'],
    data_files=[('flare_beacon/data/whoisip', [
        'flare_beacon/data/whoisip/asn_names.pkl',
        'flare_beacon/data/whoisip/ipasn.dat']),
        ('flare_beacon/data/majestic', [
            'flare_beacon/data/majestic/majestic_million.pkl']),
        ('flare_beacon/data/tld', [
            'flare_beacon/data/tld/tld_list.pkl']),
        ('flare_beacon/data/alexa', [
            'flare_beacon/data/alexa/subdomains-top1mil.txt',
            'flare_beacon/data/alexa/top-1m.csv']),
        ('flare_beacon/data/tld', [
            'flare_beacon/data/tld/tld_list.pkl']),
        ('flare_beacon/data/misc', [
            'flare_beacon/data/misc/dga_domains.txt',
            'flare_beacon/data/misc/words.csv']),
        ('flare_beacon/data/common_crawl', [
            'flare_beacon/data/common_crawl/common-crawl-1m.csv']),
        ('flare_beacon/data/umbrella', [
            'flare_beacon/data/umbrella/top-1m.csv']),
    ],
     extras_require={
        ':python_version == "2.7"': [
            'ipaddr==2.1.11',
        ],
    }
)

