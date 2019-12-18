gitclean()
{
    git filter-branch --force --index-filter "git rm --cached --ignore-unmatch $1" --prune-empty --tag-name-filter cat -- --all
}

#gitclean books/site/404.html

# gitclean books/site/404.html
# gitclean books/site/about/index.html
# gitclean books/site/css/theme.css
# gitclean books/site/css/theme_extra.css
# gitclean books/site/fonts/fontawesome-webfont.eot
# gitclean books/site/fonts/fontawesome-webfont.svg
# gitclean books/site/fonts/fontawesome-webfont.ttf
# gitclean books/site/fonts/fontawesome-webfont.woff
# gitclean books/site/img/favicon.ico
# gitclean books/site/index.html
# gitclean books/site/js/jquery-2.1.1.min.js
# gitclean books/site/js/modernizr-2.8.3.min.js
# gitclean books/site/js/theme.js
# gitclean books/site/search.html
# gitclean books/site/search/lunr.js
# gitclean books/site/search/main.js
# gitclean books/site/search/search_index.json
# gitclean books/site/search/worker.js
# gitclean books/site/sitemap.xml
# gitclean books/site/sitemap.xml.gz

# gitclean site/Dockerfile
# gitclean site/README.md
# gitclean site/VERSION
# gitclean site/generateYAML.pynb
# gitclean site/index.md
# gitclean site/manual.md
# gitclean site/requirements.txt
# gitclean site/sample.jpg
# gitclean site/setup.cfg
# gitclean site/setup.py
# gitclean site
# gitclean site1

gitclean docusaurustemplate/404.html
gitclean docusaurustemplate/about/index.html
gitclean docusaurustemplate/bumpfile.cfg
gitclean docusaurustemplate/css/theme.css
gitclean docusaurustemplate/css/theme_extra.css
gitclean docusaurustemplate/docusaurus.md
gitclean docusaurustemplate/fonts/fontawesome-webfont.eot
gitclean docusaurustemplate/fonts/fontawesome-webfont.svg
gitclean docusaurustemplate/fonts/fontawesome-webfont.ttf
gitclean docusaurustemplate/fonts/fontawesome-webfont.woff
gitclean docusaurustemplate/img/favicon.ico
gitclean docusaurustemplate/index.html
gitclean docusaurustemplate/js/jquery-2.1.1.min.js
gitclean docusaurustemplate/js/modernizr-2.8.3.min.js
gitclean docusaurustemplate/js/theme.js
gitclean docusaurustemplate/search.html
gitclean docusaurustemplate/search/lunr.js
gitclean docusaurustemplate/search/main.js
gitclean docusaurustemplate/search/search_index.json
gitclean docusaurustemplate/search/worker.js
gitclean docusaurustemplate/sitemap.xml
gitclean docusaurustemplate/sitemap.xml.gz
gitclean dest/a527f33529e503173967c4331021857e.epub
gitclean dest/all.bib
gitclean dest/book/DATACENTER/datacenter-1.md
gitclean dest/book/DATACENTER/datacenter-10.md
gitclean dest/book/DATACENTER/datacenter-11.bib
gitclean dest/book/DATACENTER/datacenter-11.md
gitclean dest/book/DATACENTER/datacenter-12.md
gitclean dest/book/DATACENTER/datacenter-13.md
gitclean dest/book/DATACENTER/datacenter-14.md
gitclean dest/book/DATACENTER/datacenter-15.md
gitclean dest/book/DATACENTER/datacenter-16.md
gitclean dest/book/DATACENTER/datacenter-17.md
gitclean dest/book/DATACENTER/datacenter-18.md
gitclean dest/book/DATACENTER/datacenter-19.md
gitclean dest/book/DATACENTER/datacenter-2.md
gitclean dest/book/DATACENTER/datacenter-20.md
gitclean dest/book/DATACENTER/datacenter-21.md
gitclean dest/book/DATACENTER/datacenter-22.md
gitclean dest/book/DATACENTER/datacenter-23.md
gitclean dest/book/DATACENTER/datacenter-3.bib
gitclean dest/book/DATACENTER/datacenter-3.md
gitclean dest/book/DATACENTER/datacenter-4.md
gitclean dest/book/DATACENTER/datacenter-5.md
gitclean dest/book/DATACENTER/datacenter-6.md
gitclean dest/book/DATACENTER/datacenter-7.md
gitclean dest/book/DATACENTER/datacenter-8.md
gitclean dest/book/DATACENTER/datacenter-9.md
gitclean dest/book/DATACENTER/datacenter.md
gitclean dest/book/DATACENTER/images/ChillD.png
gitclean dest/book/DATACENTER/images/EquinixDataCenterSG3.png
gitclean dest/book/DATACENTER/images/FBNC.png
gitclean dest/book/DATACENTER/images/FB_Prineville_DataCenter_PUE.png
gitclean dest/book/DATACENTER/images/GoogleSE.png
gitclean dest/book/DATACENTER/images/awsoutagegraph.png
gitclean dest/book/DATACENTER/images/hydro.png
gitclean dest/book/DETAILS/HEADER-DETAILS.md
gitclean dest/book/DETAILS/cloud.md
gitclean dest/book/DETAILS/health.md
gitclean dest/book/DETAILS/images/audio.png
gitclean dest/book/DETAILS/images/no.png
gitclean dest/book/DETAILS/images/presentation.png
gitclean dest/book/DETAILS/images/video.png
gitclean dest/book/DETAILS/images/warning.png
gitclean dest/book/DETAILS/intro-fall-2018.md
gitclean dest/book/DETAILS/lifestyle.md
gitclean dest/book/DETAILS/overview.md
gitclean dest/book/DETAILS/physics.md
gitclean dest/book/DETAILS/radar.md
gitclean dest/book/DETAILS/sensor.md
gitclean dest/book/DETAILS/sport.md
gitclean dest/book/DETAILS/usecases.md
gitclean dest/book/DETAILS/web.md
gitclean dest/book/ORGANIZATION/HEADER-ORGANIZATION.md
gitclean dest/book/ORGANIZATION/assignments-523.md
gitclean dest/book/ORGANIZATION/datasets.md
gitclean dest/book/ORGANIZATION/e534-i523.md
gitclean dest/book/ORGANIZATION/images/comment.png
gitclean dest/book/ORGANIZATION/images/construction.png
gitclean dest/book/ORGANIZATION/images/i523-overview.png
gitclean dest/book/ORGANIZATION/images/learning.png
gitclean dest/book/ORGANIZATION/images/smile.png
gitclean dest/book/ORGANIZATION/organization-523.md
gitclean dest/book/ORGANIZATION/plagiarism.md
gitclean dest/book/ORGANIZATION/policies.md
gitclean dest/book/ORGANIZATION/volumes.md
gitclean dest/book/PREFACE/HEADER-PREFACE.md
gitclean dest/book/PREFACE/images/audio.png
gitclean dest/book/PREFACE/images/code.png
gitclean dest/book/PREFACE/images/comment.png
gitclean dest/book/PREFACE/images/construction.png
gitclean dest/book/PREFACE/images/github.png
gitclean dest/book/PREFACE/images/idea.png
gitclean dest/book/PREFACE/images/learning.png
gitclean dest/book/PREFACE/images/no.png
gitclean dest/book/PREFACE/images/ok.png
gitclean dest/book/PREFACE/images/presentation.png
gitclean dest/book/PREFACE/images/question.png
gitclean dest/book/PREFACE/images/smile.png
gitclean dest/book/PREFACE/images/video.png
gitclean dest/book/PREFACE/images/warning.png
gitclean dest/book/PREFACE/notation.md
gitclean dest/book/PREFACE/reader.md
gitclean dest/book/cover.png
gitclean dest/book/epub.css
gitclean dest/book/ieee-with-url.csl
gitclean dest/book/metadata.txt
gitclean dest/c0bfc72630636e6b02a9fb328c38a62a.epub
gitclean dest/cbff23a6ccf84db25c29d67868508208.epub
gitclean dest

#git push origin --force --all
#git push origin --force --tags
