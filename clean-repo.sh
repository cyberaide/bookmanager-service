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

gitclean site/Dockerfile
gitclean site/README.md
gitclean site/VERSION
gitclean site/generateYAML.pynb
gitclean site/index.md
gitclean site/manual.md
gitclean site/requirements.txt
gitclean site/sample.jpg
gitclean site/setup.cfg
gitclean site/setup.py
gitclean site
gitclean site1


#git push origin --force --all
#git push origin --force --tags
