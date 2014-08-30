var App = angular.module('App', ['ui.router', 'Services']);

App.config(['$stateProvider', '$urlRouterProvider', 
	function($stateProvider, $urlRouterProvider) {

	$urlRouterProvider.otherwise("/home");

	/*$stateProvider.state('home', {
		url: "/home",
		controller: 'HomeCtrl',
		templateUrl: "/static/html/home.html"
    });*/
}]);