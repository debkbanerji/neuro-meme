angular.module('neuroMemeApp').config(['$locationProvider', '$routeProvider',
    function config($locationProvider, $routeProvider) {
        $locationProvider.hashPrefix('!');

        $routeProvider.when('/about', {
            template: '<about></about>'
        }).when('/view-memes', {
            template: '<view-memes></view-memes>'
        }).when('/classify-memes', {
            template: '<classify-memes></classify-memes>'
        }).when('/login', {
            template: '<login></login>'
        }).otherwise('/classify-memes');


        // use the HTML5 History API
        $locationProvider.html5Mode(true);
    }

]);