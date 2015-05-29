angular.module('AppCtrl')
.controller('PriceCtrl', ['$scope', 'api',
  function ($scope, api) {
    $scope.prices = [];
    api.prices.get({}, function (res) {
      if(res.prices)
        $scope.prices = res.prices;
    });

    $scope.showPrice = function () {
      $scope.priceToSave = {};
      $scope.$broadcast('showModal', 'savePrice');
    };

    $scope.editPrice = function (price) {
      $scope.priceToSave = price;
      $scope.$broadcast('showModal', 'savePrice');
    }

    $scope.onSavePrice = function (price) {
      if(price){
        $scope.prices.push(price);
      }
      $scope.$broadcast('hideModal', 'savePrice');
    }

    $scope.showDeletePrice = function (price) {
      $scope.priceToDelete = price;
      $scope.$broadcast('showModal', 'deletePrice');
    }

    $scope.deletePrice = function () {
      api.price.remove({id: $scope.priceToDelete.id}, function () {
        $scope.prices.forEach(function (value, key) {
          if(value.$$hashKey == $scope.priceToDelete.$$hashKey){
            $scope.prices.splice(key, 1);
          }
        })
        $scope.deletePriceCancel();
      })
    }
    $scope.deletePriceCancel = function () {
      $scope.$broadcast('hideModal', 'deletePrice');
    }
  }
])