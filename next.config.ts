import type { NextConfig } from "next";

const basePath = process.env.NODE_ENV === "production" ? process.env.NEXT_PUBLIC_BASE_PATH : "";

const nextConfig: NextConfig = {
  output: "export",
  basePath,
  assetPrefix: basePath,
  images: {
    unoptimized: true,
    localPatterns: [
      {
        pathname: '/public/images/**',
        search: '',
      }
    ]
  },
  trailingSlash: true,
  eslint: {
    ignoreDuringBuilds: true,
  },
  env: {
    NEXT_PUBLIC_BASE_PATH: basePath,
  },
};

export default nextConfig;
