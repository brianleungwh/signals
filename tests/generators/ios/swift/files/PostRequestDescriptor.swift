  var postPostRequestDescriptor = RKRequestDescriptor.requestDescriptorWithMapping(postRequestMapping.inverseMapping(), objectClass: PostRequest.self, rootKeyPath: nil, method: RKRequestMethodPOST)
  objectManager.addRequestDescriptor(postPostRequestDescriptor)