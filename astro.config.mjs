// @ts-check
import { defineConfig } from "astro/config";

// https://astro.build/config
export default defineConfig({
  site: "https://bossa-nova-web3-hub.vercel.app",
  build: {
    inlineStylesheets: "always",
  },
});
