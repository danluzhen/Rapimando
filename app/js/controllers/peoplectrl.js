angular.module('AppCtrl')
.controller('PeopleCtrl', ['$scope', 'api', 'conf',
  function ($scope, api, conf) {
    api.users.get({}, function (res) {
      $scope.users = res.users
    });
  }
])