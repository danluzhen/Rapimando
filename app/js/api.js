angular.module('api', ['ngResource'])
.factory('api', ['$http', '$resource', 'conf',
  function($http, $resource, conf) {
    'use strict';

    return {
      users: $resource('/_ah/api/rapimandado/v1/users', {}, {
        get: {},
        add: {method: 'POST'}
      }),
      user: $resource('/_ah/api/rapimandado/v1/users/:id', {}, {
		  update: {method: 'PUT'},
        remove: {method: 'DELETE'}
		
      }),
      prices: $resource('/_ah/api/rapimandado/v1/prices', {}, {
        get: {},
        add: {method: 'POST'}
      }),
      price: $resource('/_ah/api/rapimandado/v1/prices/:id', {}, {
        update: {method: 'PUT'},
        remove: {method: 'DELETE'}
      }),
      sites: $resource('/_ah/api/rapimandado/v1/sites', {}, {
        get: {},
        add: {method: 'POST'}
      }),
      site: $resource('/_ah/api/rapimandado/v1/sites/:id', {}, {
        update: {method: 'PUT'},
        remove: {method: 'DELETE'}
      }),
      gifts: $resource('/_ah/api/rapimandado/v1/gifts', {}, {
        get: {},
        add: {method: 'POST'}
      }),
      gift: $resource('/_ah/api/rapimandado/v1/gifts/:id', {}, {
        update: {method: 'PUT'},
        remove: {method: 'DELETE'}
      })
    };
  }]
);
