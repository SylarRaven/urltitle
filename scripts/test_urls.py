import logging
import unittest

from urltitle import config, URLTitleReader

config.configure_logging()

log = logging.getLogger(config.PACKAGE_NAME + '.' + __name__)


TEST_CASES = {
    'https://www.amazon.com/Active-Wow-Whitening-Charcoal-Natural/dp/B01N8XF244/':
        'Amazon.com : Active Wow Teeth Whitening Charcoal Powder Natural : Beauty',
    'https://www.amazon.com/gp/product/B077YCC84H/':
        'Amazon.com : Crest 3D White Whitestrips Vivid Plus : Beauty',
    'https://arxiv.org/abs/1810.04805':
        '[1810.04805] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding',
    'https://www.cell.com/cell-metabolism/fulltext/S1550-4131(18)30630-2':
        'Profound Perturbation of the Metabolome in Obesity Is Associated with Health Risk: Cell Metabolism',
    'https://www.cnn.com/2019/02/13/media/jeff-bezos-national-enquirer-leaker/index.html':
        "As questions linger around Jeff Bezos' explosive suggestions, identity of tabloid leaker is confirmed - CNN",
    'https://docs.python.org/2/library/unittest.html':
        '25.3. unittest — Unit testing framework — Python 2.7.15 documentation',
    'https://hackernoon.com/a-simple-introduction-to-pythons-asyncio-595d9c9ecf8c':
        'A simple introduction to Python’s asyncio – Hacker Noon',
    'https://www.kdnuggets.com/2019/02/ai-help-solve-humanity-challenges.html':
        'How AI can help solve some of humanity’s greatest challenges – and why we might fail',
    'https://www.marketwatch.com/story/everything-you-need-to-know-about-market-closures-on-washingtons-birthday-the-holiday-you-may-know-as-presidents-day-2019-02-15':
        'Presidents Day: Everything you need to know about market closures on Washington’s Birthday - MarketWatch',
    'https://medicalxpress.com/news/2019-01-dental-flossing-behaviors-linked-higher.html':
        'Dental flossing and other behaviors linked with higher levels of toxic chemicals in the body',
    'https://www.imdb.com/title/tt0119177/':
        'Gattaca (1997) - IMDb',
    'https://jamanetwork.com/journals/jama/fullarticle/2725150':
        'Rationing of Health Care in the United States: An Inevitable Consequence of Increasing Health Care Costs. | Health Care Economics, Insurance, Payment | JAMA | JAMA Network',
    'https://www.ncbi.nlm.nih.gov/pubmed/11204525':
        'Lycopenaemia.  - PubMed - NCBI',
    'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5334395/':
        'Fruitflow®: the first European Food Safety Authority-approved natural cardio-protective functional ingredient',
    'https://www.nbcnews.com/politics/donald-trump/trump-installs-state-art-golf-simulator-white-house-n971176':
        'Trump installs state-of-the-art golf simulator in the White House',
    'https://stackoverflow.com/questions/50842144/':
        'python - Requirements.txt greater than equal to and then less than? - Stack Overflow',
    'https://www.sciencedaily.com/releases/2019/02/190207142206.htm':
        'New pill can deliver insulin through the stomach -- ScienceDaily',
    'https://www.tandfonline.com/doi/abs/10.1080/09637486.2018.1542666':
        'Oxidation of fish oil supplements in Australia: International Journal of Food Sciences and Nutrition: Vol 0, No 0',
    'https://www.swansonvitamins.com/swanson-premium-vitamin-c-rose-hips-1000-mg-250-caps':
        'Vitamin C with Rose Hips - 1,000 mg - Swanson Health Products',
    'https://towardsdatascience.com/introducing-ubers-ludwig-5bd275a73eda':
        'Introducing Uber’s Ludwig – Towards Data Science',
    'https://www.youtube.com/watch?v=53YvP6gdD7U':
        'Deep Learning State of the Art (2019) - MIT - YouTube',
    'https://m.youtube.com/watch?v=GltlJO56S1g':
        "Jeff Bezos In 1999 On Amazon's Plans Before The Dotcom Crash - YouTube",

    # Non-HTML:
    'https://3c1703fe8d.site.internapcdn.net/newman/csz/news/800/2017/campylobacte.jpg': '(image/jpeg)',
    'https://export.arxiv.org/rss/eess.IV/recent': '(text/xml)',
    'https://static.arxiv.org/icons/cu/cornell-reduced-white-SMALL.svg': '(image/svg+xml) (10K)',
    'https://static.arxiv.org/icons/social/bibsonomy.png': '(image/png) (612B)',
    'https://arxiv.org/pdf/1902.04704.pdf': '(application/pdf) (1M)',
    'https://distill.pub/rss.xml': '(application/xml) (6K)',
    'https://download.fedoraproject.org/pub/fedora/linux/releases/29/Workstation/x86_64/iso/Fedora-Workstation-Live-x86_64-29-1.2.iso': '(application/octet-stream) (2G)',
    'https://raw.githubusercontent.com/python/cpython/master/setup.py': '(text/plain; charset=utf-8) (100K)',
    'https://i.imgur.com/2Bs7Xo6.jpg': '(image/jpeg) (980K)',
    'https://i.imgur.com/QkbaYDH.gif': '(image/gif) (553K)',
    'https://kdnuggets.com/rss': '(application/rss+xml; charset=UTF-8)',
    'https://www.sciencedaily.com/images/2019/02/190213142720_1_540x360.jpg': '(image/jpeg) (54K)',
    'https://pdfs.semanticscholar.org/4938/7632593299c040bf7628a27891cf0896ef9d.pdf': '(application/pdf) (350K)',
}

reader = URLTitleReader()


class TestURLs(unittest.TestCase):
    def test_url_titles(self):
        for url, expected_title in TEST_CASES.items():
            with self.subTest(url=url):
                self.assertEqual(expected_title, reader.title(url))
