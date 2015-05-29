angular.module('AppCtrl')
.directive('bnModal', function() {
  'use strict';

  return {
    restrict: 'E',
    transclude: true,
    scope: {
      modalId: '=',
      title: '=',
      onShown: '&',
      onHidden: '&'
    },
    link: function(scope, element) {
      element = element.find('.modal');

      scope.$on('showModal', function(event, modalId) {
        if (scope.modalId === modalId) {
          element.modal('show');
        }
      });

      scope.$on('hideModal', function(event, modalId) {
        if (scope.modalId === modalId) {
          element.modal('hide');
        }
      });

      element.on('shown.bs.modal', function() {
        scope.onShown();
      });

      element.on('hidden.bs.modal', function() {
        scope.onHidden();
      });

    },
    templateUrl: 'template/component/modal.html'
  };
});
