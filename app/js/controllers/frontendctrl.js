angular.module('AppCtrl')
.controller('FrontendCtrl', ['$scope',
  function ($scope) {
    $scope.items = [
      {date: 'Feb 1, 2015 4:30pm', userName: 'NhiemBui', driverName: 'Driver 1', from: '51, Le Dai Hanh', to: '33, Le Thanh Nghi', price: '12.3$'},
      {date: 'Feb 4, 2015 2:30pm', userName: 'ToanHoang', driverName: 'Driver 2', from: '1, Ba Trieu', to: '11, Ho Tung Mau', price: '2.5$'},
      {date: 'Feb 9, 2015 1:30pm', userName: 'Kevin', driverName: 'Driver 1', from: '55, Tran Duy Hung', to: '51, Le Dai Hanh', price: '5.7$'},
      {date: 'Feb 20, 2015 3:30pm', userName: 'Tuan', driverName: 'Driver 4', from: '123, Le Dai Hanh', to: '1, Ba Trieu', price: '7.1$'},
      {date: 'Mar 1, 2015 5:30pm', userName: 'Dinh', driverName: 'Driver 4', from: '11, Ho Tung Mau', to: '123, Le Dai Hanh', price: '4.2$'}
    ]
  }
])