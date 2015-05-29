angular.module('AppCtrl')
.controller('GiftCtrl', ['$scope', 'api',
  function ($scope, api) {
    $scope.gifts = [];
    api.gifts.get({}, function (res) {
      if(res.gifts)
        $scope.gifts = res.gifts;
    });
    
    $scope.showGift = function () {
      $scope.giftToSave = {};
      $scope.$broadcast('showModal', 'saveGift');
    };

    $scope.editGift = function (gift) {
      $scope.giftToSave = gift;
      $scope.$broadcast('showModal', 'saveGift');
    }

    $scope.onSaveGift = function (gift) {
      if(gift){
        $scope.gifts.push(gift);
      }
      $scope.$broadcast('hideModal', 'saveGift');
    }

    $scope.showDeleteGift = function (gift) {
      $scope.giftToDelete = gift;
      $scope.$broadcast('showModal', 'deleteGift');
    }

    $scope.deleteGift = function () {
      api.gift.remove({id: $scope.giftToDelete.id}, function () {
        $scope.gifts.forEach(function (value, key) {
          if(value.$$hashKey == $scope.giftToDelete.$$hashKey){
            $scope.gifts.splice(key, 1);
          }
        })
        $scope.deleteGiftCancel();
      })
    }
    $scope.deleteGiftCancel = function () {
      $scope.$broadcast('hideModal', 'deleteGift');
    }
  }
])