'use strict';

/**
 * @ngdoc directive
 * @name appApp.directive:filereader
 * @description
 * # filereader
 */
angular.module('appApp')
  .directive('fileReader', ['$parse', function ($parse) {
    return {
      restrict: 'A',
      link: function(scope, element, attributes) {
        var model = $parse(attributes.fileReader);
        element.bind('change', function(){
          scope.$apply(function(){
           model.assign(scope, element[0].files[0]);
          });
        });
      }
    };
  }]);
