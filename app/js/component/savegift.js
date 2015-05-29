angular.module('AppCtrl')
.directive('bnSaveUser', [ 'api', 'conf',
  function(api, conf) {
    'use strict';

    return {
      restrict: 'E',
      scope: {
        gift: '=',
        onDone: '='
      },
      link: function(scope) {
        scope.sites = [];
        api.sites.get({per_page: conf.perPage}, function (res) {
          if(res.sites)
            scope.sites = res.sites;
        });
        scope.$watch('gift', function () {
          if(scope.gift){
            if(scope.gift.id){
              scope.giftName = scope.gift.gift;
              scope.giftCode = scope.gift.code;
              if(scope.gift.site)
                scope.giftSite = parseInt(scope.gift.site.id)
            } else{
              scope.giftName = '';
              scope.giftCode = '';
              scope.giftSite = ''
            }
          }
        });
        scope.submitForm = function () {
          var params = {
            gift: scope.giftName,
            code: scope.giftCode,
            site: parseInt(scope.giftSite)
          };
          if(scope.gift.id){
            api.gift.update({id: scope.gift.id}, params, function (gift) {
              scope.gift.name = scope.giftName;
              scope.gift.currency_code = scope.giftCode;
              scope.gift.site = gift.site;
              scope.onDone();
            })
          } else {
            api.gifts.add(params, function (gift) {
              scope.onDone(gift);
            })
          }
        }
      },
      templateUrl: 'template/component/savegift.html'
    };
  }]
);
