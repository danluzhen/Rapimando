angular.module('AppCtrl')
.controller('SiteCtrl', ['$scope', 'api', 'conf',
  function ($scope, api, conf) {
    $scope.sites = [];
    api.sites.get({per_page: conf.perPage}, function (res) {
      if(res.sites)
        $scope.sites = res.sites;
    });

    $scope.showSite = function () {
      $scope.siteToSave = {};
      $scope.$broadcast('showModal', 'saveSite');
    }

    $scope.editSite = function (site) {
      $scope.siteToSave = site;
      $scope.$broadcast('showModal', 'saveSite');
    }

    $scope.onSaveSite = function (site) {
      if(site){
        $scope.sites.push(site);
      }
      $scope.$broadcast('hideModal', 'saveSite');
    }

    $scope.showDeleteSite = function (site) {
      $scope.siteToDelete = site;
      $scope.$broadcast('showModal', 'deleteSite');
    }

    $scope.deleteSite = function () {
      api.site.remove({id: $scope.siteToDelete.id}, function () {
        $scope.sites.forEach(function (value, key) {
          if(value.$$hashKey == $scope.siteToDelete.$$hashKey){
            $scope.sites.splice(key, 1);
          }
        })
        $scope.deleteSiteCancel();
      })
    }
    $scope.deleteSiteCancel = function () {
      $scope.$broadcast('hideModal', 'deleteSite');
    }
  }
])