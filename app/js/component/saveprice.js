angular.module('AppCtrl')
.directive('bnSavePrice', [ 'api',
  function(api) {
    'use strict';

    return {
      restrict: 'E',
      scope: {
        price: '=',
        onDone: '='
      },
      link: function(scope) {
        scope.$watch('price', function () {
          if(scope.price){
            if(scope.price.id){
              scope.priceName = scope.price.name;
              scope.priceCurrencyCode = scope.price.currency_code;
            } else{
              scope.priceName = '';
              scope.priceCurrencyCode = '';
            }
          }
        });
        scope.submitForm = function () {
          if(scope.price.id){
            api.price.update({id: scope.price.id}, {name: scope.priceName, currency_code: scope.priceCurrencyCode}, function () {
              scope.price.name = scope.priceName;
              scope.price.currency_code = scope.priceCurrencyCode;
              scope.onDone();
            })
          } else {
            api.prices.add({name: scope.priceName, currency_code: scope.priceCurrencyCode}, function (price) {
              scope.onDone(price);
            })
          }
        }
      },
      templateUrl: 'template/component/saveprice.html'
    };
  }]
);
