const routes = [
  //set route for page directions
  {
    path: "/",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/Index.vue") }],
  },
  {
    path: "/test",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/test.vue") }],
  },
  {
    path: "/comptest",
    component: () => import("layouts/MainLayout.vue"),
    children: [{ path: "", component: () => import("pages/comptest.vue") }],
  },
  {
    //this page will not have sidebar and topbar
    //since we removed the 'layouts/MainLayout.vue'
    path: "/test2",
    component: () => import("pages/test.vue"),
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: "*",
    component: () => import("pages/Error404.vue"),
  },
];

export default routes;
