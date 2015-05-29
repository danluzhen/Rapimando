var app = angular.module('RapimandadoApp', [
  'ui.bootstrap',
  'ngRoute',
  'ngResource',
  'AppCtrl',
  'api'
]);

app.config(['$locationProvider', '$routeProvider',
function($locationProvider, $routeProvider) {

  // use the HTML5 History API
  //$locationProvider.html5Mode(true);
  $routeProvider
    .when('/', {
      templateUrl: '/template/view/frontend.html',
      controller: 'FrontendCtrl',
      title: ''
    })
    .when('/people', {
      templateUrl: '/template/view/people.html',
      controller: 'PeopleCtrl',
      title: 'People'
    })
    .when('/site', {
      templateUrl: '/template/view/site.html',
      controller: 'SiteCtrl',
      title: 'Site'
    })
    .when('/price', {
      templateUrl: '/template/view/price.html',
      controller: 'PriceCtrl',
      title: 'Price'
    })
    .when('/gift', {
      templateUrl: '/template/view/gift.html',
      controller: 'GiftCtrl',
      title: 'Gift'
    })
    .when('/setting', {
      templateUrl: '/template/view/setting.html',
      controller: 'SettingCtrl',
      title: 'Setting'
    })
    .when('/user', {
      templateUrl: '/template/view/user.html',
      controller: 'UserCtrl',
      title: 'User'
    })
    .otherwise({
      redirectTo: '/'
    });
}])




