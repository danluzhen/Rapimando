angular.module('AppCtrl')
.directive('bnSaveSite', [ 'api',
  function(api) {
    'use strict';

    return {
      restrict: 'E',
      scope: {
        site: '=',
        onDone: '='
      },
      link: function(scope) {
        scope.prices = [];
        api.prices.get({}, function (res) {
          if(res.prices)
            scope.prices = res.prices;
        });
        
        scope.$watch('site', function () {
          if(scope.site){
            if(scope.site.id){
              scope.siteName = scope.site.name;
              scope.siteCountry = scope.site.country;
              scope.siteLocale = scope.site.locale;
              scope.siteAreaCode = scope.site.area_code;
              scope.siteLatitude = scope.site.latitude;
              scope.siteLongitude = scope.site.longitude;
              scope.siteGateway = scope.site.gateway;
              if(scope.site.price)
                scope.sitePrice = parseInt(scope.site.price.id);
            } else{
              scope.siteName = '';
              scope.siteCountry = '';
              scope.siteLocale = '';
              scope.siteAreaCode = '';
              scope.siteLatitude = '';
              scope.siteLongitude = '';
              scope.siteGateway = '';
              scope.sitePrice = '';
            }
          }
        });
        scope.submitForm = function () {
          var params = {
            name: scope.siteName,
            country: scope.siteCountry,
            locale: scope.siteLocale,
            area_code: scope.siteAreaCode,
            latitude: scope.siteLatitude,
            longitude: scope.siteLongitude,
            gateway: scope.siteGateway,
            price: parseInt(scope.sitePrice)
          };
          if(scope.site.id){
            api.site.update({id: scope.site.id}, params, function (site) {
              scope.site.name = scope.siteName;
              scope.site.country = scope.siteCountry;
              scope.site.locale = scope.siteLocale;
              scope.site.area_code = scope.siteAreaCode;
              scope.site.gateway = scope.siteGateway;
              scope.site.latitude = scope.siteLatitude;
              scope.site.longitude = scope.siteLongitude;
              scope.site.price = site.price;
              scope.onDone();
            })
          } else {
            api.sites.add(params, function (site) {
              scope.onDone(site);
            })
          }
        }
      },
      templateUrl: 'template/component/savesite.html'
    };
  }]
);
