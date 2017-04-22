angular.module('viewMemes').component('viewMemes', {
    templateUrl: 'view-memes/view-memes.template.html',

    controller: ['$routeParams', '$route', '$firebaseObject', '$firebaseArray', function viewMemesController($routeParams, $route, $firebaseObject, $firebaseArray) {
        var self = this;
        var user = firebase.auth().currentUser;
        self.classifiedMemesRef = firebase.database().ref().child("memes-classified");
        self.memes = $firebaseArray(self.classifiedMemesRef);
    }]
});