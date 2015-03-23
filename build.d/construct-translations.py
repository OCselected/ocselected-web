#!/bin/env python

import ConfigParser, sys, os

'''
This script takes the contents of the website-specific LINGUAS file, constructs an options menu for the languages contained therein.
It takes as argument the translations.ini relative path, the LINGUAS file relative path, and the output template name
'''

language_map = ConfigParser.ConfigParser()
language_map.readfp(open(sys.argv[1]))

banned = language_map.get('Banned', 'lang_code')

with open(sys.argv[2], 'r') as linguas: # Linguas is where available languages are stored
    with open(sys.argv[3], 'w') as output: # Output is a genshi template
        output.write('''<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
		<html xmlns="http://www.w3.org/1999/xhtml"
		  xmlns:py="http://genshi.edgewall.org/"
		  xmlns:xi="http://www.w3.org/2001/XInclude"
		  py:strip="">

		<!-- This file is generated, don't edit here -->

		''')
        output.write('''
		<script type="text/javascript">
		/* This list is generated, don't edit here */
		$(function() {
			$( '.uls-trigger' ).uls( {
				onSelect : function( language ) {
					var languageName = $.uls.data.getAutonym( language );
					$( '.uls-trigger' ).text( languageName );
                    $('#selectedLang').val(language);
                    $('#langSelect').trigger('submit');
				},
				languages: { 'en' : 'English' ''')
        try:
            for lang in linguas:
                lang = lang.strip()
                if lang and not lang.startswith('#') and not lang in banned:
                    #output.write('    <option value="' + lang + '" py:attrs="{\'selected\': lang == \'' + lang + '\' and \'selected\' or None}">' + language_map.get('Languages',lang) + '</option>\n')
                    output.write(", '"+lang+"': '"+language_map.get('Languages',lang)+"'")
        finally:
            linguas.close()
        output.write("""}
			} );
		} );
		</script>
		""")
        output.write('</html>')
