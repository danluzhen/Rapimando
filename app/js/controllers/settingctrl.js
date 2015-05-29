angular.module('AppCtrl')
.controller('SettingCtrl', ['$scope', 'api', 'conf',
  function ($scope, api, conf) {
    $scope.setting = {
      distance: 50
    }

    $scope.saveDistance = function () {
      $scope.$broadcast('hideModal', 'setupDistance');
    }
  }
])