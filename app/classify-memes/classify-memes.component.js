angular.module('classifyMemes').component('classifyMemes', {
    templateUrl: 'classify-memes/classify-memes.template.html',

    controller: ['$routeParams', '$route', '$firebaseObject', '$firebaseArray', function classifyMemesController($routeParams, $route, $firebaseObject, $firebaseArray) {
        var self = this;
        var user = firebase.auth().currentUser;
        self.trainMemesRef = firebase.database().ref().child("memes-train");
        self.memes = $firebaseArray(self.trainMemesRef);

        self.upvoteSpiciness = function (target) {
            // console.log(target);
            memeRef = self.trainMemesRef.child(target.key);
            memeRef.child("spiciness").set(target.spiciness + 1)
        };
        self.upvoteDankness = function (target) {
            // console.log(target);
            memeRef = self.trainMemesRef.child(target.key);
            memeRef.child("dankness").set(target.dankness + 1)
        }
    }]
});