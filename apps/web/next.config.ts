import type { NextConfig } from "next"

const nextConfig: NextConfig = {
    output: "standalone",
    images: {
        remotePatterns: [
            {
                protocol: "http",
                hostname: "image-server",
                port: "80",
                pathname: "/**"
            },
            {
                protocol: "http",
                hostname: "localhost",
                port: "8080",
                pathname: "/**"
            },
            {
                protocol: "http",
                hostname: "host.docker.internal",
                port: "8080",
                pathname: "/**"
            }
        ],
        dangerouslyAllowLocalIP: true,
    }
}

export default nextConfig
