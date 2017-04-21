angular.module('viewMemes').component('viewMemes', {
    templateUrl: 'view-memes/view-memes.template.html',

    controller: ['$routeParams', '$route', '$firebaseObject', '$firebaseArray', function viewMemesController($routeParams, $route, $firebaseObject, $firebaseArray) {
        var self = this;
        var user = firebase.auth().currentUser;
        self.viewMemesRef = firebase.database().ref().child("users").child(user.uid).child("view-memes");
    }]
});