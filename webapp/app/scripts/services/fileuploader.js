'use strict';

/**
 * @ngdoc service
 * @name appApp.fileuploader
 * @description
 * # fileuploader
 * Service in the appApp.
 */
angular.module('appApp')
  .service('fileuploader', [ '$http', function ($http) {
    return {
      upload: function(file, url, cb) {
        var formData = new FormData();
        formData.append('datafile', file);
        $http.post(url, formData, {
          transformRequest: angular.identity,
          headers: {
            'Content-Type': undefined
          }
        })
        .then(function(response) { // success callback
          cb(JSON.parse(response.data));
        }, function(response) { // error callback
          cb(JSON.parse(response.data));
        });
      }
    }
  }]);
