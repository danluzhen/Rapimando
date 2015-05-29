angular.module('AppCtrl')
.controller('UserCtrl', ['$scope', 'api', 'conf',
 
  
  function ($scope, api,conf) {
    $scope.users = [];
    api.users.get({}, function (res) {
      if(res.users)
        $scope.users = res.users;
    });

    $scope.showUser = function () {
      $scope.userToSave = {};
      $scope.$broadcast('showModal', 'saveUser');
    };

    $scope.editUser = function (user) {
      $scope.userToSave = user;
      $scope.$broadcast('showModal', 'saveUser');
    }

    $scope.onSaveUser = function (user) {
      if(user){
        $scope.users.push(user);
      }
      $scope.$broadcast('hideModal', 'saveUser');
    }

    $scope.showDeleteUser = function (user) {
      $scope.userToDelete = user;
      $scope.$broadcast('showModal', 'deleteUser');
    }

    $scope.deleteUser = function () {
      api.user.remove({id: $scope.userToDelete.id}, function () {
        $scope.users.forEach(function (value, key) {
          if(value.$$hashKey == $scope.userToDelete.$$hashKey){
            $scope.users.splice(key, 1);
          }
        })
        $scope.deleteUserCancel();
      })
    }
    $scope.deleteUserCancel = function () {
      $scope.$broadcast('hideModal', 'deleteUser');
    }
  }
])