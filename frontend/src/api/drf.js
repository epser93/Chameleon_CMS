export default{
    // domain : 'http://127.0.0.1:8000',
    domain : 'http://k3c205.p.ssafy.io',
    // URL: 'http://127.0.0.1:8000/api/',
    URL: 'http://k3c205.p.ssafy.io/api/',
    ROUTER: {
      //user
      userinfo: 'accounts/',
      login: 'accounts/login/',
      signup: 'accounts/signup/',
      logout: 'accounts/logout/',
      usermanage : 'accounts/manage/',
      accountvalidation: 'accounts/validation',
      
      // department
      department : 'accounts/department/',

      // user search
      usersearch : 'accounts/search/',

      // log
      log : 'accounts/logs/',

      // event
      event: 'services/event/',
      
      // category
      category : 'products/categories/', 

      // item
      item : 'products/product/',
      itemhistory : 'products/temp_product/',
      history: 'products/',

      // notice
      notice : 'services/notices/',

      // main
      main : 'services/main/',
      carousel : 'services/carousel/',

      // customer
      customer : {

        // main
        main : 'services/customer/main/',
        carousel : 'services/customer/carousel/',

        // product
        category : 'products/customer/categories/',
        item : 'products/customer/product/',

        // event
        event : 'services/customer/event/',

        // search
        search : 'services/customer/search/?content=',
        
      }
    }
  }