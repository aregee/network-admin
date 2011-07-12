/*
 * Copyright (C) 2011 Adriano Monteiro Marques
 *
 * Author: Piotrek Wasilewski <wasilewski.piotrek@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

if(!window.jQuery) {
	throw 'jQuery not found';
}

jQuery(function($) {

	$('#results').ajaxError(function(e, xhr){
		console.log(e);
		console.log(xhr);
	});
	
	umit = {};
	umit.api = {};
	
	umit.api.settings = {
		'API_URL': 'http://localhost/api/'
	}
	
	umit.api.getHosts = function() {
		var get_url = umit.api.settings['API_URL'] + 'host/list/';
		$.get(umit.api.settings['API_URL'] + 'host/list/', function(d){
			console.log(d.hosts);
		}, "json");
	}

	umit.api.getHosts();
});