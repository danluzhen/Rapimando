angular.module('AppCtrl')
  .directive('bnNavBar', [ '$location',
    function($location) {
      'use strict';

      return {
        restrict: 'E',
        scope: {},
        link: function(scope) {
          scope.isActive = function (viewLocation) {
            return viewLocation === $location.path();
          };
        },
        templateUrl: 'template/component/navbar.html'
      };
    }]
);
