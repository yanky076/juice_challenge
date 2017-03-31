'use strict';

describe('Service: fileuploader', function () {

  // load the service's module
  beforeEach(module('appApp'));

  // instantiate service
  var fileuploader;
  beforeEach(inject(function (_fileuploader_) {
    fileuploader = _fileuploader_;
  }));

  it('should do something', function () {
    expect(!!fileuploader).toBe(true);
  });

});
