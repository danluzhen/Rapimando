angular.module('AppCtrl')
  .directive('bnUserStatus', [ 'api',
    function(api) {
      'use strict';

      return {
        restrict: 'E',
        scope: {
          user: '='
        },
        link: function(scope) {
          if(!scope.user.status){
            scope.user.status = 'active'
          }

          scope.$watch('user.status', function () {
            api.user.update({id: scope.user.id}, {status: scope.user.status})
          })
        },
        templateUrl: 'template/component/userstatus.html'
      };
    }]
);
