'use strict';

/**
 * @ngdoc function
 * @name appApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the appApp
 */
angular.module('appApp')
  .controller('MainCtrl', ['$scope', 'fileuploader', '$window', function ($scope, fileuploader, $window) {
    this.awesomeThings = [
      'HTML5 Boilerplate',
      'AngularJS',
      'Karma'
    ];

    $scope.onFormSubmit = function() {
      fileuploader.upload($scope.file, '/upload', function(response){
        if(response.response_code == 200) {
          $scope.parsedData = JSON.parse(response.response_msg);
        } else {
          $window.alert(response.response_msg);
        }
      });
    }
  }]);
