angular.module('classifyMemes').component('classifyMemes', {
    templateUrl: 'classify-memes/classify-memes.template.html',

    controller: ['$routeParams', '$route', '$firebaseObject', '$firebaseArray', function classifyMemesController($routeParams, $route, $firebaseObject, $firebaseArray) {
        var self = this;
        var user = firebase.auth().currentUser;
        self.classifyMemesRef = firebase.database().ref().child("users").child(user.uid).child("classify-memes");
    }]
});